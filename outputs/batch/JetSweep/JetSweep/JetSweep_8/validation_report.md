# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_8`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 26 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [104–121], lower_priority='Action_ZoneBlock' annotated_start=105, effective_Action_ZoneBlock_start=122.
> - Action 'Action_None' range [104-217] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-64] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-90] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [105-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [108-111] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-261] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-156] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [104-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [124-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-260] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-217] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [134-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [96-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [117-209] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [213-214] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [227-230] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [233-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-164] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-141] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-192] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-214] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [219-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-269] for track '20' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.