# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_46`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 94: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [172–188], lower_priority='Action_ZoneBlock' annotated_start=174, effective_Action_ZoneBlock_start=189.
> - Action 'Action_PreSnap' range [0-91] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-173] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-349] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-304] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-228] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-271] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-280] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-361] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-202] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-166] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-275] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-273] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [226-231] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [233-240] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [249-250] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [253-254] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-39] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [182-244] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [250-251] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [172-179] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' for track '11' starts at frame 203, but the player has no visible bounding box on this frame.
> - Action 'Action_BlockSecondLevel' range [203-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [205-206] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-274] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-289] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-322] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-282] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-257] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-306] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-342] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-416] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-242] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-258] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-276] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-327] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-281] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-289] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-323] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-380] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-361] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-367] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-391] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-343] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-303] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-418] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [302-419] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-387] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-421] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-343] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-347] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-387] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-366] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-372] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-479] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-409] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-479] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-391] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [394-432] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-440] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-474] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-477] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-470] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-475] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-479] for track '41' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.