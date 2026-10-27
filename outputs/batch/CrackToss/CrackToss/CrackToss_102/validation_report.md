# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_102`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_102/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 249 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 202: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 202: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 202: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
> - Action 'Action_None' range [118-200] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-173] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [148-219] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-249] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-249] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-242] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-249] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-185] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-220] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-140] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-142] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-131] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [123-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [163-165] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-243] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-241] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-236] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '29' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.