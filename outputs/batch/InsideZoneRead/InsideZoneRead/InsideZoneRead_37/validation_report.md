# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_37`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 137 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 76: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
> - Segment 'Action_BallCarry' for track '7' has invalid range: start=162, end=150. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [119–132], lower_priority='Action_ZoneBlock' annotated_start=121, effective_Action_ZoneBlock_start=133.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 110 frames exceeds threshold 90 frames [start=121, end=230].
> - Action 'Action_None' range [119-375] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-404] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-223] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-198] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-291] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-318] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-364] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-398] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-327] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-232] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-255] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-386] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-400] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-244] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-272] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-354] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-295] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-327] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-388] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [394-419] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-192] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-285] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-318] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-291] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-263] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-270] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-359] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-375] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-251] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-200] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-337] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-283] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-339] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-343] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-361] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-419] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-276] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-312] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-419] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-331] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-357] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-419] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-172] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-186] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-253] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-263] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-278] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-331] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-352] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-360] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-396] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [404-406] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-321] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-355] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-368] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-390] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [401-402] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-419] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-324] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-340] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-358] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-376] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-381] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-388] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-377] for track '35' has 2 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.