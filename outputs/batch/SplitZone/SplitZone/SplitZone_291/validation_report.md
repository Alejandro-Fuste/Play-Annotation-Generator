# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_291`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_291/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 584: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [17–30], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=31.
> - Action 'Action_None' range [17-131] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-66] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-99] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-161] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-170] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-87] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-118] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-167] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [41-60] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-70] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-177] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-131] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-53] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [72-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [34-52] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-188] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-14] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [21-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [60-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [99-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [166-170] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [177-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [182-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [26-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-48] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-90] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-193] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-206] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-99] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-209] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-202] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '39' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.