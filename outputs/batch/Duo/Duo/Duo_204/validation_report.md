# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_204`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_204/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 17 |
| Player Tracks | 16 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 36 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-201] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-216] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-222] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-194] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-225] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [171-191] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [199-225] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [169-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [169-195] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 198, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [198-207] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '15' has 2 frames without a visible bounding box.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.