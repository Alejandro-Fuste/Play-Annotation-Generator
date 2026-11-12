# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_51`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 133 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [80–95], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=96.
> - Segment 'Action_BlockSecondLevel' for track '21' has invalid range: start=112, end=73. Clamping end to start.
> - Action 'Action_None' range [80-171] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-240] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-256] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-276] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-290] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-327] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-284] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-294] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-313] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-99] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-110] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [90-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-327] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [107-294] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [296-298] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [326-327] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-310] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-278] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-297] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-319] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-290] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-276] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-252] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-292] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-302] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-95] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-297] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-123] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [125-136] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-278] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-290] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-318] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-49] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-28] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-67] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-79] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-91] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-187] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-137] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-218] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-236] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-252] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-326] for track '39' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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