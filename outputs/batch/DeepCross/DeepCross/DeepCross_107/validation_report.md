# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_107`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_107/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 110: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [27–42], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=43.
> - Action 'Action_BallCarry' range [215-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-173] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-220] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-190] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-194] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-285] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-143] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-177] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-119] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-115] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-244] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-159] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [163-178] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-232] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-246] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-260] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-280] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-317] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-176] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [157-182] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-66] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-254] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-21] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-181] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-184] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-185] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.