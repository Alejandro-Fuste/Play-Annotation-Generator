# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_101`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_101/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 128 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-218] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [216-220] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [222-228] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-179] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-110] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-45] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-79] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-105] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-79] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-149] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-79] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-66] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-79] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-207] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-79] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-74] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-176] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [180-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [183-217] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-68] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-68] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-68] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-109] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-218] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-174] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-232] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-239] for track '30' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-182] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-215] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-125] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-138] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-142] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-156] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-178] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-194] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-218] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-170] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-218] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-193] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-192] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-203] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-231] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-239] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-239] for track '46' has 2 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.