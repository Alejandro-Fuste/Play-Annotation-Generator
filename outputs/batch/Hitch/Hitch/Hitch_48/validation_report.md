# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_48`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [1–12], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=13.
> - Action 'Action_None' range [1-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-27] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-157] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-123] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-165] for track '4' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-202] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunHitchRoute' range [14-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [201-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-55] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [146-147] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-195] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-151] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-36] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-113] for track '20' has 9 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [146-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '21' starts at frame 4, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [4-4] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-47] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-99] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-149] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-134] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-131] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-163] for track '26' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.