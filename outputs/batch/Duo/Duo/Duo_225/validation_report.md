# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_225`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_225/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '10' has invalid range: start=123, end=89. Clamping end to start.
> - Action 'Action_PreSnap' range [0-200] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [123-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [129-132] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [141-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [144-152] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-181] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-199] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-200] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [123-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-77] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-169] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-79] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-118] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-200] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-197] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-200] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.