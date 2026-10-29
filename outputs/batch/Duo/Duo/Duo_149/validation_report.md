# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_149`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_149/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-233] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-230] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-153] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-224] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-202] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-234] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [131-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [157-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-239] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [131-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [140-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [150-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [156-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-239] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.