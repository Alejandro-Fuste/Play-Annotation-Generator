# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_155`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_155/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [61–73], lower_priority='Action_ZoneBlock' annotated_start=63, effective_Action_ZoneBlock_start=74.
> - Action 'Action_None' range [61-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-217] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-168] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-125] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-222] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-230] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-233] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [61-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-209] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-232] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-239] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-96] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-156] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-191] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-202] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-164] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-205] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-154] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-86] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [116-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-205] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-227] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-239] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-237] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '29' has 1 frames without a visible bounding box.
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