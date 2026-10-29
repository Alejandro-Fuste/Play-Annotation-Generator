# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_26`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_26/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-121] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-162] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-170] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-170] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [96-117] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [119-136] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [93-147] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-164] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-59] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-81] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-89] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-140] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-52] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-65] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-152] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-151] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.