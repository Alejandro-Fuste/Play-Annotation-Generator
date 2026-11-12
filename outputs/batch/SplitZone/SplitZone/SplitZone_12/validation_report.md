# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_12`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 28 |
| Ball Tracks | 2 |
| CSV events parsed | 22 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [290–295], lower_priority='Action_ZoneBlock' annotated_start=294, effective_Action_ZoneBlock_start=296.
> - Segment 'Action_SnapReceive' for track '15' has invalid range: start=290, end=115. Clamping end to start.
> - Segment 'Action_Handoff' for track '15' has invalid range: start=317, end=115. Clamping end to start.
> - Action 'Action_PreSnap' range [13-289] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-449] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-366] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [370-387] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-405] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [313-341] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [294-318] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [320-355] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-384] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-343] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-215] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-336] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-417] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [331-444] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [318-320] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [296-334] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [337-342] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [344-345] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [347-373] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-115] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-449] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-326] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-449] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-449] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-449] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-399] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-440] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-399] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-418] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [420-425] for track '28' has 2 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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