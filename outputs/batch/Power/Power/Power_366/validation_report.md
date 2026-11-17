# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_366`
- **Input XML**: `outputs/batch/Power/Power/Power_366/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [3-263] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-267] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-282] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-221] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-245] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-274] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [203-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-270] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-329] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-250] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-329] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [203-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [238-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-275] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-92] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-259] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-288] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-300] for track '29' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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