# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_229`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_229/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Overlapping action conflict at frame 58 for track '11': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [57–69], lower_priority='Action_ZoneBlock' annotated_start=58, effective_Action_ZoneBlock_start=70.
> - Action 'Action_BallCarry' range [83-230] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [234-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-146] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-153] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-182] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-268] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [57-238] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-256] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-265] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-269] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [58-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-139] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-137] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-187] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-211] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-233] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-183] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-244] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '19' starts at frame 70, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [70-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-84] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-113] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-203] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.