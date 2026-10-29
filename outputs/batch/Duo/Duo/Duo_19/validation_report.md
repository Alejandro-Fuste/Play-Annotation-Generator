# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_19`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_19/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-209] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-209] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-209] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-177] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-125] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-181] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [132-164] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [132-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-166] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-192] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-209] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.