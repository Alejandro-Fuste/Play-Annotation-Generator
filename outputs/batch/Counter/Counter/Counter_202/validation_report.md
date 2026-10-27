# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_202`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_202/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 405: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [86-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-139] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-116] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [88-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-159] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-121] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-197] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-264] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-212] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-269] for track '27' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.