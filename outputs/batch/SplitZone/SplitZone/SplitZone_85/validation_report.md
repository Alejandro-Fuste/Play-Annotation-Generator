# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_85`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 99 frames exceeds threshold 90 frames [start=213, end=311].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (RG) duration 99 frames exceeds threshold 90 frames [start=213, end=311].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [210–231], lower_priority='Action_ZoneBlock' annotated_start=213, effective_Action_ZoneBlock_start=232.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 99 frames exceeds threshold 90 frames [start=213, end=311].
> - Action 'Action_None' range [210-275] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-263] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-293] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [297-389] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-338] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-389] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-293] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-376] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-253] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [264-268] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-298] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-267] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-234] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-286] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-273] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-232] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [252-262] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [264-265] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [286-290] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-389] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 240, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [240-244] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [210-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [246-266] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [268-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-209] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [210-235] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-306] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-358] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-385] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-369] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-275] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-385] for track '26' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [341-346] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-389] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.