# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_243`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_243/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 130 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 486: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [14–30], lower_priority='Action_ZoneBlock' annotated_start=17, effective_Action_ZoneBlock_start=31.
> - Action 'Action_None' range [14-43] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-49] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-89] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-122] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-43] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-59] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-49] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-43] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-203] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-234] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-230] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-223] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-224] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [56-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-206] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-215] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-46] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-216] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-232] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-49] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-62] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-239] for track '27' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-215] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-234] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-175] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-193] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-189] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-208] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-215] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '39' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.