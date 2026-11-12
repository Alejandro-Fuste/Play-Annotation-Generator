# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_149`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_149/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 131 frames exceeds threshold 90 frames [start=138, end=268].
> - Validation warning: Action 'Action_BlockSecondLevel' for track '16' (C) duration 92 frames exceeds threshold 90 frames [start=177, end=268].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 131 frames exceeds threshold 90 frames [start=138, end=268].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 131 frames exceeds threshold 90 frames [start=138, end=268].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 131 frames exceeds threshold 90 frames [start=138, end=268].
> - Action 'Action_None' range [135-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-358] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-306] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-315] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-265] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-303] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-359] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [145-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [186-268] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [167-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [171-342] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-321] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-335] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-355] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-204] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-262] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [266-294] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [177-268] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-334] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-355] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-238] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [241-243] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-244] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-315] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-291] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-304] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-312] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-325] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-336] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-348] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-357] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-349] for track '28' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.