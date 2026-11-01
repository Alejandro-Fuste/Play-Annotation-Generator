# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_265`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_265/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [17–31], lower_priority='Action_ZoneBlock' annotated_start=20, effective_Action_ZoneBlock_start=32.
> - Action 'Action_None' range [17-208] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-147] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-197] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-231] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-170] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [174-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-103] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-214] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-119] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-208] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-214] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-94] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-163] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-214] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [69-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-211] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-52] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-100] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-231] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-223] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-107] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-208] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-226] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-226] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-237] for track '44' has 1 frames without a visible bounding box.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.