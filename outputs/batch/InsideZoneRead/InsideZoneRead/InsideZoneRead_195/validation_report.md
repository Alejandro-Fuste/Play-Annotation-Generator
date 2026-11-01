# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_195`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_195/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [191–206], lower_priority='Action_ZoneBlock' annotated_start=194, effective_Action_ZoneBlock_start=207.
> - Action 'Action_PreSnap' range [0-164] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-288] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-297] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-212] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-282] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-265] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-235] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-241] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-257] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [218-232] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-368] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [191-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [220-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [241-242] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [244-246] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [248-250] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [253-259] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-293] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-310] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-302] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-281] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-307] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-377] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-371] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-340] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-328] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-386] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-389] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-370] for track '28' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.