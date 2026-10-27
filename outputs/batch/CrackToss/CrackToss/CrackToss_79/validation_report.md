# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_79`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 160: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [75-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-200] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-117] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-200] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [108-199] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [78-138] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-194] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-200] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-147] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [154-200] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-181] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-96] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-4] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-11] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-22] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-9] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-92] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [92-115] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [94-129] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-200] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-171] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-200] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '29' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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