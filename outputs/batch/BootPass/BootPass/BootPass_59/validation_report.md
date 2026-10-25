# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_59`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 48 |
| Player Tracks | 48 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 157 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 98: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [27–41], lower_priority='Action_RunBlock' annotated_start=35, effective_Action_RunBlock_start=42.
> - Action 'Action_None' range [162-274] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-358] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-203] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-333] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-287] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-301] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-92] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-119] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-133] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [135-266] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-314] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-218] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-245] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-253] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [27-40] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [49-336] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-181] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-321] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-52] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [54-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [57-64] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-247] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-359] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [63-355] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [357-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-322] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-334] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [48-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [64-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-359] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-328] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-51] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-254] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-304] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-344] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-359] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-234] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [100-167] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-165] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-287] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-146] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-191] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-286] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-248] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-283] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-359] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-359] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-262] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-305] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-353] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-272] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-285] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-287] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-312] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-328] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-335] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-340] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-345] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-359] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-322] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-313] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-340] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-327] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-359] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-327] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-334] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-356] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '47' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.