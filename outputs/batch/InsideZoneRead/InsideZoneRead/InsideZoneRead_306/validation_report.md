# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_306`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_306/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [10-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-61] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-247] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [250-253] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-92] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-87] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-40] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-155] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-269] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-221] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-228] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-48] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-259] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-161] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [10-209] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-186] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-16] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-228] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-259] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-195] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-237] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-242] for track '28' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.