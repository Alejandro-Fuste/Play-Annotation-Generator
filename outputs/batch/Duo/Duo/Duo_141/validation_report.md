# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_141`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_141/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [125-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [146-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [125-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-198] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-211] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-162] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-225] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.