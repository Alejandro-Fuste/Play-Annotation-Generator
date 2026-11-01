# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_361`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_361/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 155 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [26–39], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=40.
> - Action 'Action_None' range [26-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-239] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [26-69] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-219] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-110] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-196] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-221] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [54-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [68-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-213] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-61] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-93] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-108] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-155] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-222] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-108] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-204] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-220] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-110] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [118-123] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-196] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-230] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-195] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-192] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-203] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-220] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-222] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '41' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.