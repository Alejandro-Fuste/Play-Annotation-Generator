# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_46`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 24 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 94: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [136-175] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-175] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-161] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [164-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-175] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [112-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-127] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-173] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-139] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-175] for track '24' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.