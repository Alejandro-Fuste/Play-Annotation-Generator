# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_231`
- **Input XML**: `outputs/batch/Power/Power/Power_231/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 464: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [7-139] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-235] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-341] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-345] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-237] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-355] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-214] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-326] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-275] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-359] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-271] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-340] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-244] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-335] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-345] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-355] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [183-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-337] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [183-238] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-326] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-337] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-359] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-283] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-337] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-289] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-348] for track '26' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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