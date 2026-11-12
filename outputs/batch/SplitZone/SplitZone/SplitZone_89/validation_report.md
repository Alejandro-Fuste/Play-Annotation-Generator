# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_89`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 156 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 180: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (LT) duration 119 frames exceeds threshold 90 frames [start=158, end=276].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [155–158], lower_priority='Action_ZoneBlock' annotated_start=158, effective_Action_ZoneBlock_start=159.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 119 frames exceeds threshold 90 frames [start=158, end=276].
> - Action 'Action_None' range [155-381] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-387] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-396] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-420] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [423-427] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-432] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-447] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-256] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-285] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-297] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-368] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-336] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-389] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [391-396] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-403] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-415] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [419-422] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-379] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-208] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-227] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [233-276] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-374] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-416] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-422] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-449] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [189-276] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-314] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-340] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-352] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-387] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-394] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-411] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-420] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-431] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-449] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-414] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [416-419] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-222] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-247] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-263] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-379] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [382-385] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-394] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [403-404] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-414] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-420] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-439] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-166] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [185-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-234] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [160-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [204-243] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [249-250] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [254-255] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [260-271] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-390] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-387] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [402-403] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-411] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-414] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-333] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '20' starts at frame 158, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [158-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [182-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-276] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-318] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-327] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-387] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-396] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-421] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [432-449] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-449] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-211] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-394] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-421] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [424-426] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-449] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-252] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-384] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-406] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-413] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-449] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-283] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-305] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-320] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-402] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-270] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-317] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-396] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-389] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-396] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-406] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-414] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-427] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [429-443] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [353-374] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-429] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [431-447] for track '32' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.