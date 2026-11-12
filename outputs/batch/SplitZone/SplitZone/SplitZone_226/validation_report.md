# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_226`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_226/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 152 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 118 frames exceeds threshold 90 frames [start=146, end=263].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 118 frames exceeds threshold 90 frames [start=146, end=263].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 118 frames exceeds threshold 90 frames [start=146, end=263].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [143–157], lower_priority='Action_ZoneBlock' annotated_start=146, effective_Action_ZoneBlock_start=158.
> - Action 'Action_SnapReceive' range [143-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [163-166] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [168-171] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-156] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-188] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-92] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 143, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [143-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-170] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-262] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [143-218] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-242] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-259] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-419] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-197] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-402] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [184-186] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [210-240] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [245-249] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-320] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-324] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-419] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_SplitBlock' for track '6' starts at frame 149, but the player has no visible bounding box on this frame.
> - Action 'Action_SplitBlock' range [149-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-160] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [173-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-156] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-46] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-409] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [182-213] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [215-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [224-256] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [258-260] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [262-397] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [399-408] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-10] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-245] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-266] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-280] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-338] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-364] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-377] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-387] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-156] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-166] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-326] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-335] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-356] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-377] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-15] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [143-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [176-177] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [197-203] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [211-213] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-245] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-419] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-419] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-419] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-258] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-366] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [368-371] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-397] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-401] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-418] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-296] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-363] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-335] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-385] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-339] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-366] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [368-384] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-408] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-360] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-368] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-385] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [390-402] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-408] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-417] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-386] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-409] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [413-415] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.