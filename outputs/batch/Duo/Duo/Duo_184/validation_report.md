# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_184`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_184/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 26 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-129] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [86-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [86-93] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [97-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [104-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-36] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-52] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-104] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '26' has 1 frames without a visible bounding box.
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