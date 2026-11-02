# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_168`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_168/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [21-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-170] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-193] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [23-61] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-49] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-142] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-102] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-163] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-188] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-76] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-116] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-48] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '16' starts at frame 23, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [23-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-172] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [68-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [87-198] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [200-209] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-100] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-161] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-197] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '32' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.