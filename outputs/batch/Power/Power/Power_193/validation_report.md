# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_193`
- **Input XML**: `outputs/batch/Power/Power/Power_193/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 388: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 388: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [22-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-232] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-229] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-111] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-198] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-120] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-197] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-155] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-94] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-122] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-188] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-166] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-181] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-196] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-193] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-207] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-239] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '31' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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