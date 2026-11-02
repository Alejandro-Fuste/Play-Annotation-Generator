# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_59`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [45–58], lower_priority='Action_ZoneBlock' annotated_start=52, effective_Action_ZoneBlock_start=59.
> - Action 'Action_None' range [45-145] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-157] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-176] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-83] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [83-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [105-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-70] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [45-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [64-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 83, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [83-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-224] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-73] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [53-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [79-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-260] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-186] for track '31' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.