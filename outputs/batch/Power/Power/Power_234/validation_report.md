# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_234`
- **Input XML**: `outputs/batch/Power/Power/Power_234/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 25 |
| Ball Tracks | 1 |
| CSV events parsed | 12 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PreSnap' range [9-414] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-425] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-352] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-421] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [257-271] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-438] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-321] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-404] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-439] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-119] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [257-262] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-449] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [257-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [275-287] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [289-293] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-351] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-365] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-400] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-430] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-264] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-404] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-427] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [431-449] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-449] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-404] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-411] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-425] for track '24' has 3 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.