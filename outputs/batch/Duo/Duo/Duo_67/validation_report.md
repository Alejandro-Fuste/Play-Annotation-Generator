# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_67`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
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
> - Action 'Action_PreSnap' range [0-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-183] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [124-138] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-209] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-145] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-209] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-188] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-207] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-146] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [124-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-209] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-29] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-101] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-67] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-208] for track '26' has 1 frames without a visible bounding box.
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