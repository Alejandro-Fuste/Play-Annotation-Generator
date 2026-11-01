# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_121`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_121/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [76-247] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-214] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-241] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [124-151] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-207] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-187] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-261] for track '29' has 1 frames without a visible bounding box.
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