# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_82`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 124 frames exceeds threshold 90 frames [start=240, end=363].
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 124 frames exceeds threshold 90 frames [start=240, end=363].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 110 frames exceeds threshold 90 frames [start=240, end=349].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [237–252], lower_priority='Action_ZoneBlock' annotated_start=240, effective_Action_ZoneBlock_start=253.
> - Action 'Action_PreSnap' range [30-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-312] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-355] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-353] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-317] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-344] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-368] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-330] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-367] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [240-330] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-479] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-342] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [240-265] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [305-313] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [319-333] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-415] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [242-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-380] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-277] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [300-328] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [347-349] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [353-355] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-267] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [268-299] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-271] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [240-265] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [270-284] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [338-349] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [253-268] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-236] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-262] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-277] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-350] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-332] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-350] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-359] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-292] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-355] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-342] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-479] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-443] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [296-376] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-350] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-331] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-371] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [364-369] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-452] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.