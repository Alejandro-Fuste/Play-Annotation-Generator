# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_105`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_105/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 212: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '13' has invalid range: start=154, end=153. Clamping end to start.
> - Action 'Action_PreSnap' range [0-265] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-309] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-312] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-319] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-328] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-268] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-212] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-192] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-330] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-260] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-307] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-317] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-390] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-108] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-281] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-218] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-46] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-107] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-126] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-213] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-74] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [158-168] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-231] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-419] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-256] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-274] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-419] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-216] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-242] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-203] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-218] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-231] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-251] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-259] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-272] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-284] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-316] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-324] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-230] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-291] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-247] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-247] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-262] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-309] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-326] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-301] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-350] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-353] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-356] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-319] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-334] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-365] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-333] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-378] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-385] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-413] for track '38' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-367] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-394] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-402] for track '41' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.