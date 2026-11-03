# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_67`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [6–20], lower_priority='Action_PassBlock' annotated_start=9, effective_Action_PassBlock_start=21.
> - Action 'Action_BallCarry' range [106-218] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [221-225] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [229-232] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [234-243] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-205] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [170-219] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [224-242] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [250-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-132] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-211] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-218] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-203] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-42] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-264] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [57-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-211] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [115-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-66] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '26' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.