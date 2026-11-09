# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_171`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_171/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_Handoff' for track '18' has invalid range: start=80, end=77. Clamping end to start.
> - Action 'Action_PreSnap' range [0-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-112] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-169] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-109] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-239] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-164] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-219] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-32] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-59] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [66-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [74-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-21] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-30] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-167] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-191] for track '24' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.