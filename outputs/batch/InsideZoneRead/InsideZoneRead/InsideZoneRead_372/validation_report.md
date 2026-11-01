# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_372`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_372/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=19.
> - Segment 'Action_BallCarry' for track '11' has invalid range: start=59, end=50. Clamping end to start.
> - Action 'Action_None' range [3-156] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-84] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-24] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-60] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-115] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-178] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-63] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-195] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-23] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-32] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-165] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-215] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [27-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [40-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [43-50] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-239] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-19] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-38] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-70] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-97] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-117] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-232] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-140] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-155] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-165] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-199] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-207] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-199] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-238] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-187] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-231] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-195] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-239] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '39' has 1 frames without a visible bounding box.
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