# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_15`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
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
> - Row 32: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-156] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [105-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [135-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-179] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-178] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [119-162] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-156] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-129] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-179] for track '21' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-179] for track '23' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '25' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.