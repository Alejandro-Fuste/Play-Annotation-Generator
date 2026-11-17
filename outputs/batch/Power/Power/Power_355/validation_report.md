# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_355`
- **Input XML**: `outputs/batch/Power/Power/Power_355/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 710: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 710: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [13-239] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-239] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-133] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-116] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-238] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-235] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [76-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-129] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-239] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-127] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [76-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-164] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-178] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-203] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-222] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-239] for track '25' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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