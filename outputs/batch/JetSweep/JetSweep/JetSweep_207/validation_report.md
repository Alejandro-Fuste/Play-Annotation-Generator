# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_207`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_207/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [65–75], lower_priority='Action_ZoneBlock' annotated_start=66, effective_Action_ZoneBlock_start=76.
> - Action 'Action_None' range [65-154] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-150] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-204] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-269] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-163] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-235] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-252] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-267] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-184] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-170] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-90] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [65-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-207] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-217] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-259] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-105] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-171] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-183] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-231] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-269] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-148] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-234] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-246] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-249] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.