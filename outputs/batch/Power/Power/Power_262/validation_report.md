# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_262`
- **Input XML**: `outputs/batch/Power/Power/Power_262/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 91 frames exceeds threshold 90 frames [start=82, end=172].
> - Validation warning: Action 'Action_PullBlock' for track '11' (LT) duration 91 frames exceeds threshold 90 frames [start=82, end=172].
> - Action 'Action_PreSnap' range [22-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-199] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-126] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-188] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-239] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-62] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-91] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-228] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-137] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-201] for track '18' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.