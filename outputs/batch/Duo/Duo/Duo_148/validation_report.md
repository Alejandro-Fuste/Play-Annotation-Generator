# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_148`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_148/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '13' has invalid range: start=87, end=82. Clamping end to start.
> - Action 'Action_PreSnap' range [0-136] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-179] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-163] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-179] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [87-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [119-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [129-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-179] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-179] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-164] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [112-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-45] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-179] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-137] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-162] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-179] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-159] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-179] for track '23' has 2 frames without a visible bounding box.
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
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.