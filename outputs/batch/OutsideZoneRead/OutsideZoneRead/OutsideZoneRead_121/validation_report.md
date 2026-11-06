# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_121`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_121/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [35–48], lower_priority='Action_ZoneBlock' annotated_start=38, effective_Action_ZoneBlock_start=49.
> - Action 'Action_None' range [35-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-141] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-173] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-59] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-86] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-109] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-142] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-77] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-61] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-66] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-66] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-74] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-160] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-138] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-172] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [35-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-74] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [56-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [77-174] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [176-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-61] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-80] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-74] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-141] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '37' has 1 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.