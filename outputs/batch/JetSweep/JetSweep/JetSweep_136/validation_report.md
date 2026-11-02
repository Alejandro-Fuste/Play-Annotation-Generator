# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_136`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_136/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [48–60], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=61.
> - Action 'Action_None' range [48-71] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-248] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-68] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-104] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-132] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-95] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-93] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-178] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [49-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [69-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-260] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-131] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [48-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '14' starts at frame 61, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [61-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [80-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-139] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-165] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-178] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-267] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-235] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-238] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-248] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-260] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '33' has 1 frames without a visible bounding box.
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