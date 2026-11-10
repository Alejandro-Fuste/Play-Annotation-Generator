# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_29`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-125] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-130] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-113] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-119] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [120-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [124-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [164-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-180] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '25' has 1 frames without a visible bounding box.
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