# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_41`
- **Input XML**: `outputs/batch/Power/Power/Power_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [23-172] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-203] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-175] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-187] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-187] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-172] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-224] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-237] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-179] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-178] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-178] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-170] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-198] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-231] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-120] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-179] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-188] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.